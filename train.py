import torch
from utils import AverageMeter,save_model,output_state
import sys
import time
import numpy as np
from sklearn.metrics import f1_score
from config import parse_option
import os
from utils import set_loader, set_model, set_optimizer, adjust_learning_rate


def train_supervised(train_loader, model,criterion, optimizer, epoch, opt):
    """one epoch training"""
    model.train()


    batch_time = AverageMeter()
    data_time = AverageMeter()
    losses = AverageMeter()
    device = opt.device
    end = time.time()

    for idx, (image, bio_tensor) in enumerate(train_loader):
        data_time.update(time.time() - end)

        images = image.to(device)

        labels = bio_tensor.float()

        labels = labels.to(device)
        bsz = labels.shape[0]

        # compute loss


        output = model(images)
        loss = criterion(output, labels)

        # update metric
        losses.update(loss.item(), bsz)

        # SGD
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # measure elapsed time
        batch_time.update(time.time() - end)
        end = time.time()

        # print info
        if (idx + 1) % opt.print_freq == 0:
            print('Train: [{0}][{1}/{2}]\t'.format(
                epoch, idx + 1, len(train_loader)))

            sys.stdout.flush()
## dd
            # Calculate and print F1 score
   # sample_evaluation(train_loader, model, opt)
## dd
    return losses.avg

def submission_generate(val_loader, model, opt):
    """validation"""
    model.eval()

    device = opt.device
    out_list = []
    with torch.no_grad():
        for idx, (image) in (enumerate(val_loader)):# for idx, (image,bio_tensor) in (enumerate(val_loader)):

            images = image.float().to(device)

            # forward
            output = model(images)
            output = torch.round(torch.sigmoid(output))
            out_list.append(output.squeeze().detach().cpu().numpy())


    out_submisison = np.array(out_list)
    np.save('output',out_submisison)


def sample_evaluation(val_loader, model, opt):
    """validation"""
    model.eval()

    device = opt.device
    out_list = []
    label_list = []
    with torch.no_grad():
        for idx, image in (enumerate(val_loader)):

            images = image.float().to(device)
            labels = bio_tensor.float()

            labels = labels.float()

            label_list.append(labels.squeeze().detach().cpu().numpy())
            # forward
            output = model(images)
            output = torch.round(torch.sigmoid(output))
            out_list.append(output.squeeze().detach().cpu().numpy())

    label_array = np.array(label_list)
    out_array = np.array(out_list)
    f = f1_score(label_array,out_array,average='macro')
    print(f)


def main():
    opt = parse_option()

    # build data loader
    train_loader,test_loader = set_loader(opt)

    # build model and criterion
    model, criterion = set_model(opt)

    # build optimizer
    optimizer = set_optimizer(opt, model)


    # training routine
    for epoch in range(1, opt.epochs + 1):
        train_supervised(train_loader, model, criterion, optimizer, epoch, opt)
    '''
    # Print train loss after each epoch
        print(f"Epoch [{epoch}/{opt.epochs}] - Train Loss: {train_loss:.4f}")
        
        # Evaluate model's training and print F1 score
        sample_evaluation(train_loader, model, opt)

    '''
    submission_generate(test_loader, model, opt)
    #sample_evaluation(test_loader, model, opt)

    save_file = os.path.join(
        opt.save_folder, 'last.pth')
    save_model(model, optimizer, opt, opt.epochs, save_file)

    global output_csv_name
    output_csv_name=output_state(opt.model,opt.batch_size,opt.epochs,opt.learning_rate,opt.momentum,opt.temp)

    ###edited by dd
    txt_file_path = '/kaggle/working/output_csv_name.txt'
    try:
        with open(txt_file_path, 'w') as file:
            file.write(output_csv_name)
        print("csv name file created successfully.")
    except Exception as e:
        print("Error creating file:", e)
    ###

   # global output_csv_name='a'#str(model)#+str(opt.epochs)+str(opt.batch_size) #this line is added to output name for csv.use this vairable only.
   # return a
if __name__ == '__main__':
    main()
