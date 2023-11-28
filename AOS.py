# AOS+CE
def AOS_CE(out_logits, origlabs, tarlabs, weight):
    t = weight
    basemask = (1./t) * torch.ones_like(out_logits.detach()).cuda()
    tarmask = torch.sign(torch.gather(out_logits, -1, tarlabs.unsqueeze(1)))*F.one_hot(tarlabs, 1000)
    orimask = torch.sign(torch.gather(out_logits, -1, origlabs.unsqueeze(1)))*F.one_hot(origlabs, 1000)
    basemask[tarmask > 0] = 1./t**2
    basemask[tarmask < 0] = t
    basemask[orimask > 0] = t    
    basemask[orimask < 0] = 1./t**2
    loss = nn.CrossEntropyLoss(reduction='sum')(out_logits*basemask, tarlabs)
    return loss 


# AOS+Po_Trip
def AOS_PoTrip(out_logits, origlabs, tarlabs, weight):
    t = weight
    basemask = (1./t) * torch.ones_like(out_logits.detach()).cuda()
    tarmask = torch.sign(torch.gather(out_logits, -1, tarlabs.unsqueeze(1)))*F.one_hot(tarlabs, 1000)
    orimask = torch.sign(torch.gather(out_logits, -1, origlabs.unsqueeze(1)))*F.one_hot(origlabs, 1000)
    basemask[tarmask > 0] = 1./t**2
    basemask[tarmask < 0] = t
    basemask[orimask > 0] = t
    basemask[orimask < 0] = 1./t**2
    tarlabs_onehot = torch.zeros(out_logits.shape[0], 1000).cuda()
    tarlabs_onehot.scatter_(1, tarlabs.unsqueeze(1), 1)
    origlabs_onehot = torch.zeros(out_logits.shape[0], 1000).cuda()
    origlabs_onehot.scatter_(1, origlabs.unsqueeze(1), 1)
    dis_logits = basemask * out_logits  
    loss_po = Poincare_dis(dis_logits / torch.sum(torch.abs(dis_logits), 1, keepdim=True),torch.clamp((tarlabs_onehot - 0.00001), 0.0, 1.0))
    loss_cos = torch.clamp(Cos_dis(tarlabs_onehot, dis_logits) - Cos_dis(origlabs_onehot, dis_logits) + 0.007, 0.0, 2.1)
    loss=loss_po + 0.01 * loss_cos
    return loss
