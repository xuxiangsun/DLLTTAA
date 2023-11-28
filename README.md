## On Single-Model Transferable Targeted Attacks: A Closer Look at Decision-Level Optimization

This repo contains the codes for our paper published at IEEE TIP, entitled "[On Single-Model Transferable Targeted Attacks: A Closer Look at Decision-Level Optimization](https://ieeexplore.ieee.org/abstract/document/10129225)", by Xuxiang Sun, Gong Cheng, Hongda Li, Lei Pei, and Junwei Han.

> **Abstract:** *Known as a hard nut, the single-model transferable targeted attacks via decision-level optimization objectives have attracted much attention among scholars for a long time. On this topic, recent works devoted themselves to designing new optimization objectives. In contrast, we take a closer look at the intrinsic problems in three commonly adopted optimization objectives, and propose two simple yet effective methods in this paper to mitigate these intrinsic problems. Specifically, inspired by the basic idea of adversarial learning, we, for the first time, propose a unified Adversarial Optimization Scheme (AOS) to release both the problems of gradient vanishing in cross-entropy loss and gradient amplification in Po+Trip loss, and indicate that our AOS, a simple transformation on the output logits before passing them to the objective functions, can yield considerable improvements on the targeted transferability. Besides, we make a further clarification on the preliminary conjecture in Vanilla Logit Loss (VLL) and point out the problem of unbalanced optimization in VLL, in which the source logit may risk getting increased without the explicit suppression on it, leading to the low transferability. Then, the Balanced Logit Loss (BLL) is further proposed, where we take both the source logit and the target logit into account. Comprehensive validations witness the compatibility and the effectiveness of the proposed methods across most attack frameworks, and their effectiveness can also span two tough cases ( i.e ., the low-ranked transfer scenario and the transfer to defense methods) and three datasets ( i.e ., the ImageNet, CIFAR-10, and CIFAR-100).*

#### Quick Start
We provide the codes regarding AOS+CE and AOS+PoTrip in `./AOS.py`. You can incorporate the loss in your own framework directly. Similarly, BLL loss is offered in `./BLL.py`.

#### Citation
If you think this repository may be helpful to you, please consider giving a star :star: and citation. Thanks for your consideration.
```
@article{sun2023single,
  author={Sun, Xuxiang and Cheng, Gong and Li, Hongda and Pei, Lei and Han, Junwei},
  journal={IEEE Transactions on Image Processing}, 
  title={On Single-Model Transferable Targeted Attacks: A Closer Look at Decision-Level Optimization}, 
  year={2023},
  volume={32},
  pages={2972-2984}
}
```
