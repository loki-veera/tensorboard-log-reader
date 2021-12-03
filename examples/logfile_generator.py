import torch.utils.tensorboard as tb

writer = tb.writer.SummaryWriter()
for number in range(10):
    writer.add_scalar('linear_1', scalar_value=number, global_step=number)

for number in range(25):
    writer.add_scalar('linear_2', scalar_value=number, global_step=number)