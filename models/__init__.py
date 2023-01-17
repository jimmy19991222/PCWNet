from models.pwcnet import PWCNet_G, PWCNet_GC, PWCNet_wo_fine_GC, PWCNet_wo_fine_G
from models.loss import model_loss

__models__ = {
    "gwcnet-g": PWCNet_G,
    "gwcnet-gc": PWCNet_GC,
    "gwcnet-wo_fine_gc": PWCNet_wo_fine_GC,
    "gwcnet-wo_fine_g": PWCNet_wo_fine_G
}
