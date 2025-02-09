from enum import unique, Enum


@unique
class Nets(Enum):
    cifar100_resnet = "Cifar100ResNet"
    cifar100_vgg = "Cifar100VGG"
    cifar10_cnn = "Cifar10CNN"
    cifar10_resnet = "Cifar10ResNet"
    fashion_mnist_cnn = "FashionMNISTCNN"
    fashion_mnist_resnet = "FashionMNISTResNet"
    mnist_cnn = 'MNISTCNN'
