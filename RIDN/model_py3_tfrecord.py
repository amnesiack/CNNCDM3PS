import time

from utils_py3_tfrecord import *
from model_database import *

class denoiser(object):
    def __init__(self, sess, input_c_dim=3, batch_size=64, patch_size=160):
        self.sess = sess
        self.input_c_dim = input_c_dim
        self.Y_ = tf.placeholder(tf.float32, [None, None, None, self.input_c_dim], name='GroundTruth') # ground truth
        self.X = tf.placeholder(tf.float32, [None, None, None, self.input_c_dim], name='BilinearInitialization') # input of the network
        self.is_training = tf.placeholder(tf.bool, name='is_training')
        
        self.Y = CIR_RIDN(self.X, is_training=self.is_training)
        init = tf.global_variables_initializer()
        self.sess.run(init)
        print("[*] Initialize model successfully...")

    def test(self, test_files_gt, test_files_bl, ckpt_dir, save_dir):
        # init variables
        tf.global_variables_initializer().run()
        assert len(test_files_gt) != 0, 'No testing data!'
        load_model_status, global_step = self.load(ckpt_dir)
        assert load_model_status == True, '[!] Load weights FAILED...'
        print("[*] Load weights SUCCESS...")
        psnr_sum = 0
        psnr_initial_sum = 0
        test_sum = 0
        ssim_sum = 0
        csnr_sum = np.zeros(3)
        for idx in range(len(test_files_gt)):
            imagename = os.path.basename(test_files_gt[idx])
            clean_image = load_images(test_files_gt[idx]).astype(np.float32)
            _, w, h, _  = clean_image.shape
            image_bayer = load_images(test_files_bl[idx]).astype(np.float32)
            image_bayer_crop = image_bayer[:, 0:w//2*2, 0:h//2*2, :]
            test_s_time = time.time()
            output_clean_image = self.sess.run(self.Y, feed_dict={self.X: image_bayer_crop, self.is_training: False})
            test_time = time.time()-test_s_time
            
            output_clean_image1 = image_bayer.copy() # deal with the odd width and height issues
            output_clean_image1[:, 0:w//2*2, 0:h//2*2, :] = output_clean_image

            groundtruth = np.clip(clean_image, 0, 255).astype('uint8')
            noisyimage = np.around(np.clip(image_bayer, 0, 255)).astype('uint8')
            outputimage = np.around(np.clip(output_clean_image1, 0, 255)).astype('uint8')
            psnr_bilinear = imcpsnr(groundtruth, noisyimage, 255)
            psnr = imcpsnr(groundtruth, outputimage, 255)
            csnr = impsnr(groundtruth, outputimage, 255)
            ssim = MS_SSIM(groundtruth, outputimage)
            print("%s, Noisy PSNR: %.2fdB, Final PSNR: %.2fdB, MS-SSIM: %.5f, Time: %.4fs" % (imagename, psnr_bilinear, psnr, ssim, test_time))
            psnr_sum += psnr
            psnr_initial_sum += psnr_bilinear
            csnr_sum += csnr
            ssim_sum += ssim
            test_sum += test_time
            save_images(os.path.join(save_dir, imagename), outputimage)
        avg_psnr = psnr_sum / len(test_files_gt)
        avg_psnr_initial = psnr_initial_sum / len(test_files_gt)
        avg_ssim = ssim_sum / len(test_files_gt)
        avg_csnr = csnr_sum / len(test_files_gt)
        print("--- Test --- Average PSNR Noisy: %.2fdB , Final: %.2fdB (R: %.2f, G: %.2f, B: %.2f), MS-SSIM: %.5f, Running Time: %.4fs ---" % (avg_psnr_initial, avg_psnr,avg_csnr[0], avg_csnr[1], avg_csnr[2], avg_ssim, test_sum))

    def load(self, checkpoint_dir):
        print("[*] Reading checkpoint...")
        saver = tf.train.Saver()
        ckpt = tf.train.get_checkpoint_state(checkpoint_dir)
        if ckpt and ckpt.model_checkpoint_path:
            full_path = tf.train.latest_checkpoint(checkpoint_dir)
            global_step = int(full_path.split('/')[-1].split('-')[-1])
            saver.restore(self.sess, full_path)
            return True, global_step
        else:
            return False, 0
