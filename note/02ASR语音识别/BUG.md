### egs/digist

> [Kaldi for Dummies教程](http://fancyerii.github.io/kaldidoc/kaldi-for-dummy/)

- kaldi::KaldiFatalErrorerror getting feature dimension

  mfcc特征提取问题，检查`data/train/split1/1/feats.scp`路径下feats文件是否存在

  ```shell
  utils/validate_data_dir.sh data/train # 检查训练声学模型需要的数据是否合乎要求
  utils/fix_data_dir.sh # 尝试fix它们
  # 参考其他实例修改mfcc提取代码，提示错误信息：conf/mfcc.conf 错误
  # mfccdir=mfcc
  # for x in train test; do
  #   steps/make_mfcc.sh --cmd "$train_cmd" --nj 2 data/$x exp/make_mfcc/$x $mfccdir || exit 1;
  #   steps/compute_cmvn_stats.sh data/$x exp/make_mfcc/$x $mfccdir || exit 1;
  #   utils/fix_data_dir.sh data/$x || exit 1;
  # done
  ```

  总结：注意后缀名 mfcc.conf；decode.conf和decode.config
  
- refusing to split data because number of speakers 1 is less than the number of output .scp files 2

  ```
  修改为nj=1，可能是因为数据量过小的原因
  ```

- steps/decode.sh: Not scoring because local/score.sh does not exist or not executable.

  ```
  去kaldi/egs/voxforge/s5/local把score.sh复制到local下。注意这里的local不是data/local而是根目录digits/local
  ```

### egs/magic_comp

> [智源 — MagicSpeechNet 家庭场景中文语音数据集挑战赛 基于KALDI的语音识别基线系统](https://www.biendata.com/models/category/4283/L_notebook/)

- 修改`data_prep.sh`完成数据准备工作

  ```
  # 修改数据路径为绝对路径
  corpus_dir=/home/li/kaldi/egs/magic_comp/s5/Magicdata
  # 运行
  bash data_prep.sh
  ```

- 修改`run.sh`完成特征提取和帧对齐

  - 添加conf文件，mfcc.conf和decode.config

  - 缺少命令选项

    ```
    dictdir=data/local/dict
    dir=data/local/lm
    text=data/train
    
    bash local/train_lms_srilm.sh $dictdir $dir $text|| exit 1;
    ```

    

