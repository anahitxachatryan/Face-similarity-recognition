import torch
import torchvision.transforms as transforms
import torchvision.datasets as datasets
import torch.nn.functional as F
from torch.utils.data import DataLoader, Dataset

from .siameseNet import SiameseNetwork
from .createDataset import SiameseNetworkDataset

def dataLoader(pathToData):
    folder_dataset_test = datasets.ImageFolder(root=pathToData)
    transformation = transforms.Compose([transforms.Resize((100,100)),
                                        transforms.ToTensor()])
    siamese_dataset_test = SiameseNetworkDataset(imageFolderDataset=folder_dataset_test,
                                            transform=transformation)
    test_dataloader = DataLoader(siamese_dataset_test, num_workers=0, batch_size=1, shuffle=True)

    return test_dataloader

def loadModel(pathToModel):
    net_loaded = SiameseNetwork()
    net_loaded.load_state_dict(torch.load(pathToModel, map_location='cpu'))
    return net_loaded

def runModel(pathToData,pathToModel):
    net_loaded = loadModel(pathToModel)
    test_dataloader = dataLoader(pathToData)
    dataiter = iter(test_dataloader)
    x0, _ = next(dataiter)
    _, x1 = next(dataiter)
    output1, output2 = net_loaded(x0, x1)
    euclidean_distance = F.pairwise_distance(output1, output2)
    return euclidean_distance.item()




