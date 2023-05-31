from sewar.full_ref import mse, rmse, psnr, uqi, ssim, ergas, scc, rase, sam, msssim, vifp
import cv2

image1 = cv2.imread("okul_logo.png")
image2 = cv2.imread("new_img.png")

print("MSE: ", mse(image1,image2))
print("RMSE: ", rmse(image1, image2))
print("PSNR: ", psnr(image1, image2))
print("SSIM: ", ssim(image1, image2))
print("UQI: ", uqi(image1, image2))
print("MSSSIM: ", msssim(image1, image2))
print("ERGAS: ", ergas(image1, image2))
print("SCC: ", scc(image1, image2))
print("RASE: ", rase(image1, image2))
print("SAM: ", sam(image1, image2))
print("VIF: ", vifp(image1, image2))