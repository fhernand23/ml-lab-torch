# https://www.learnopencv.com/pytorch-for-beginners-image-classification-using-pre-trained-models/
from torchvision import models
from torchvision import transforms
import torch
from PIL import Image

googlenet = models.googlenet(pretrained=True)
# print(googlenet)

transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],std=[0.229, 0.224, 0.225])])
# [1]: Here we are defining a variable transform which is a combination of all the image transformations to be carried out on the input image.
# [2]: Resize the image to 256×256 pixels.
# [3]: Crop the image to 224×224 pixels about the center.
# [4]: Convert the image to PyTorch Tensor data type.
# [5-7]: Normalize the image by setting its mean and standard deviation to the specified values.

for fimg in ["dog.jpg","futbol.jpg","bike.jpg","truck.jpg"]:
    print(fimg)
    img = Image.open(fimg)

    img_t = transform(img)
    batch_t = torch.unsqueeze(img_t, 0)

    googlenet.eval()

    out = googlenet(batch_t)
    # print(out.shape)

    with open('imagenet_classes.txt') as f:
        classes = [line.strip() for line in f.readlines()]

    # _, index = torch.max(out, 1)
    percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100

    _, indices = torch.sort(out, descending=True)
    [print(classes[idx], percentage[idx].item()) for idx in indices[0][:5]]

