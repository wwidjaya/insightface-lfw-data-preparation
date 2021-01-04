"""
    If you find InsightFace useful in your research, please consider to cite the following related papers:

    @inproceedings{deng2019retinaface,
    title={RetinaFace: Single-stage Dense Face Localisation in the Wild},
    author={Deng, Jiankang and Guo, Jia and Yuxiang, Zhou and Jinke Yu and Irene Kotsia and Zafeiriou, Stefanos},
    booktitle={arxiv},
    year={2019}
    }

    @inproceedings{guo2018stacked,
    title={Stacked Dense U-Nets with Dual Transformers for Robust Face Alignment},
    author={Guo, Jia and Deng, Jiankang and Xue, Niannan and Zafeiriou, Stefanos},
    booktitle={BMVC},
    year={2018}
    }

    @article{deng2018menpo,
    title={The Menpo benchmark for multi-pose 2D and 3D facial landmark localisation and tracking},
    author={Deng, Jiankang and Roussos, Anastasios and Chrysos, Grigorios and Ververas, Evangelos and Kotsia, Irene and Shen, Jie and Zafeiriou, Stefanos},
    journal={IJCV},
    year={2018}
    }

    @inproceedings{deng2018arcface,
    title={ArcFace: Additive Angular Margin Loss for Deep Face Recognition},
    author={Deng, Jiankang and Guo, Jia and Niannan, Xue and Zafeiriou, Stefanos},
    booktitle={CVPR},
    year={2019}
    }

"""

import pickle
import os
import lfw
from util import CommonUtil as cu

def pack_lfw(args):
  lfw_dir = args.data_dir
  image_dir = args.image_dir
  lfw_pairs = lfw.read_pairs(os.path.join(lfw_dir, 'pairs.txt'))
  lfw_paths, issame_list = lfw.get_paths(image_dir, lfw_pairs, 'jpg')
  lfw_bins = []
  i = 0

  filebar = cu.get_secondary_bar(values=lfw_paths, bar_desc='Overall packing progress')
  for path in filebar:
    with open(path, 'rb') as fin:
      _bin = fin.read()
      lfw_bins.append(_bin)
      i+=1
    filebar.refresh()

  with open(args.output, 'wb') as f:
    pickle.dump((lfw_bins, issame_list), f, protocol=pickle.HIGHEST_PROTOCOL)
