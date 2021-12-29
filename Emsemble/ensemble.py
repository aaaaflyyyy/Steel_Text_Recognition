import numpy as np
def read_result(model):
    lines = []
    model_result = {}

    if model is None:
        with open('./submission_template_private.csv', 'r') as fr:
            lines = fr.readlines()
        for l in lines[1:]:
            model_result[l.split(',')[0]] = [' ' , '-1']
    else:
        with open(f'./private_test_result/private_test_result({model}c).csv', 'r') as fr:
            lines = fr.readlines()
        for l in lines[1:]:
            model_result[l.split(',')[0]] = [ l.split(',')[1] , l.split(',')[2][:-1]]

    return model_result

templates = []
with open('./submission_template_private.csv', 'r') as fr:
    templates  = fr.readlines()
    fr.close()
filenames = []
for t in templates[1:]:
    filenames.append(t.split(',')[0])


models = ('1633681189', '1634452643', '1635693541', '1635575738', '1635412054', '1635673426')
# value for the max conf. of voted pred. - max conf. of all pred. should less than
thr = 1

model_num = len(models)
model_A,model_B,model_C,model_D,model_E,model_F,model_G,model_H = None,None,None,None,None,None,None,None

# read model
if model_num == 1:
    model_A, = models
    ans_file = f'{model_A}'
elif model_num == 2:
    model_A,model_B = models
    ans_file = f'{model_A}_{model_B}'
elif model_num == 3:
    model_A,model_B,model_C = models
    ans_file = f'{model_A}_{model_B}_{model_C}'
elif model_num == 4:
    model_A,model_B,model_C,model_D = models
    ans_file = f'{model_A}_{model_B}_{model_C}_{model_D}'
elif model_num == 5:
    model_A,model_B,model_C,model_D,model_E = models
    ans_file = f'{model_A}_{model_B}_{model_C}_{model_D}_{model_E}'
elif model_num == 6:
    model_A,model_B,model_C,model_D,model_E,model_F = models
    ans_file = f'{model_A}_{model_B}_{model_C}_{model_D}_{model_E}_{model_F}'
elif model_num == 7:
    model_A,model_B,model_C,model_D,model_E,model_F,model_G = models
    ans_file = f'{model_A}_{model_B}_{model_C}_{model_D}_{model_E}_{model_F}_{model_G}'
elif model_num == 8:
    model_A,model_B,model_C,model_D,model_E,model_F,model_G,model_H = models
    ans_file = f'{model_A}_{model_B}_{model_C}_{model_D}_{model_E}_{model_F}_{model_G}_{model_H}'
else:
    print(model_num)

# read result
model_A_result = read_result(model_A)
model_B_result = read_result(model_B)
model_C_result = read_result(model_C)
model_D_result = read_result(model_D)
model_E_result = read_result(model_E)
model_F_result = read_result(model_F)
model_G_result = read_result(model_G)
model_H_result = read_result(model_H)

with open(f'private_ans({model_num}_{thr}_vote).csv','w') as fw:
    fw.write('id,text\n')

    for k in filenames:

        model_A_conf , model_A_pred = eval(model_A_result[k][1]) , str(model_A_result[k][0])
        model_B_conf , model_B_pred = eval(model_B_result[k][1]) , str(model_B_result[k][0])
        model_C_conf , model_C_pred = eval(model_C_result[k][1]) , str(model_C_result[k][0])
        model_D_conf , model_D_pred = eval(model_D_result[k][1]) , str(model_D_result[k][0])
        model_E_conf , model_E_pred = eval(model_E_result[k][1]) , str(model_E_result[k][0])
        model_F_conf , model_F_pred = eval(model_F_result[k][1]) , str(model_F_result[k][0])
        model_G_conf , model_G_pred = eval(model_G_result[k][1]) , str(model_G_result[k][0])
        model_H_conf , model_H_pred = eval(model_H_result[k][1]) , str(model_H_result[k][0])

        conf_list = [model_A_conf,model_B_conf,model_C_conf,model_D_conf,model_E_conf,model_F_conf,model_G_conf,model_H_conf]
        pred_list = [model_A_pred,model_B_pred,model_C_pred,model_D_pred,model_E_pred,model_F_pred,model_G_pred,model_H_conf]

        conf_list , pred_list = conf_list[:model_num] , pred_list[:model_num]

        preds , cnt = np.unique(pred_list,return_counts=True)
        if max(cnt) > 1 and len(preds[np.where(cnt == max(cnt))]) == 1 and abs(max(conf_list) - max([conf_list[i] for i in range(model_num) if pred_list[i] == preds[np.where(cnt == max(cnt))][0]])) < thr:
            final_ans = preds[np.where(cnt == max(cnt))][0]
        else:
            # choose ans
            if model_A_conf == max(conf_list):
                final_ans = model_A_pred
            elif model_B_conf == max(conf_list):
                final_ans = model_B_pred
            elif model_C_conf == max(conf_list):
                final_ans = model_C_pred
            elif model_D_conf == max(conf_list):
                final_ans = model_D_pred
            elif model_E_conf == max(conf_list):
                final_ans = model_E_pred
            elif model_F_conf == max(conf_list):
                final_ans = model_F_pred
            elif model_G_conf == max(conf_list):
                final_ans = model_G_pred
            else:
                final_ans = model_H_pred

        if final_ans:
            print(f'{k},{final_ans}')
            fw.write(f'{k},{final_ans}\n')
        else:
            print(f'{k}, ')
            fw.write(f'{k}, \n')
    fw.close()