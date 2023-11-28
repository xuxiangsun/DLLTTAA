def BLL(out_logits, origlabs, tarlabs):    
    real = out_logits.gather(1,tarlabs.unsqueeze(1)).squeeze(1)
    orig = out_logits.gather(1,origlabs.unsqueeze(1)).squeeze(1)
    logit_dists = (-1 * real) + orig
    loss = logit_dists.sum()
    return loss
