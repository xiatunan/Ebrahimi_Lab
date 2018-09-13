# -*- coding: utf-8 -*-
# author: Tunan Xia
# Date: Aug 22nd 2018
# for Ebrahimi Lab

import os
import numpy as np
import xlrd as xr
import Tkinter as tk
from scipy import interpolate
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

####################
root = tk.Tk()
root.title('baselinebox')
root.geometry('512x512')
root.update()
varf = tk.StringVar()
vard = tk.StringVar()
varln = tk.StringVar()
varh = tk.StringVar()
varp = tk.StringVar()
varst = tk.StringVar()
vare = tk.StringVar()
varpa = tk.StringVar()

e_f = tk.Entry(root, textvariable=varf)
varf.set('data filename')
e_f.place(x=16, y=16, width=160, height=32)

e_d = tk.Entry(root, textvariable=vard)
vard.set('cols or rows')
e_d.place(x=16, y=48, width=160, height=32)

e_ln = tk.Entry(root, textvariable=varln)
varln.set('line number')
e_ln.place(x=16, y=80, width=160, height=32)

e_h = tk.Entry(root, textvariable=varh)
varh.set('number of header lines')
e_h.place(x=16, y=112, width=160, height=32)

e_p = tk.Entry(root, textvariable=varp)
varp.set('background line')
e_p.place(x=16, y=144, width=160, height=32)

e_s = tk.Entry(root, textvariable=varst)
varst.set('start point')
e_s.place(x=16, y=176, width=160, height=32)

e_e = tk.Entry(root, textvariable=vare)
vare.set('end point')
e_e.place(x=16, y=208, width=160, height=32)

e_pa = tk.Entry(root, textvariable=varpa)
varpa.set('segment number')
e_pa.place(x=16, y=240, width=160, height=32)


def hit():
    global filename, dim, line_number, header, pbs, start, end, parts
    filename = str(varf.get().strip())
    dim = str(vard.get().strip())
    line_number = int(varln.get().strip())
    header = int(varh.get().strip())
    pbs = int(varp.get().strip())
    start = float(varst.get().strip())
    end = float(vare.get().strip())
    parts = int(varpa.get().strip())


b_a = tk.Button(root, text='apply', command=hit)
b_a.place(x=16, y=272, width=160, height=32)
####################


def col_selector(xl, xh):
    excel_data = xr.open_workbook(str(filename))
    table_raw = excel_data.sheets()[0]
    ncols = table_raw.ncols
    nrows = table_raw.nrows
    data = []
    tables = table_raw.col_values(xl)
    for i in range(nrows - xh):
        data.append(tables[i + xh])
    return data


def col_title(xl):
    excel_data = xr.open_workbook(str(filename))
    table_raw = excel_data.sheets()[0]
    ncols = table_raw.ncols
    nrows = table_raw.nrows
    tables = table_raw.col_values(xl)
    tits = str(tables[0])
    return tits


def col_base(T, xh, xs, xe):
    excel_data = xr.open_workbook(str(filename))
    table_raw = excel_data.sheets()[0]
    ncols = table_raw.ncols
    nrows = table_raw.nrows
    axisline = table_raw.col_values(0)
    initial = 0
    final = len(axisline) - xh
    for i in range(len(axisline) - xh):
        a0 = axisline[i + xh]
        d0 = abs(axisline[xh + 2] - axisline[xh + 1])
        if abs(xs - a0) <= d0/2.0:
            initial = i
        if abs(xe - a0) <= d0/2.0:
            final = i
        else:
            continue
    base = T[initial:final]
    return base


def row_selector(xl, xh):
    excel_data = xr.open_workbook(str(filename))
    table_raw = excel_data.sheets()[0]
    ncols = table_raw.ncols
    nrows = table_raw.nrows
    data = []
    tables = table_raw.row_values(xl)
    for i in range(ncols - xh):
        data.append(tables[i + xh])
    return data


def row_title(xl):
    excel_data = xr.open_workbook(str(filename))
    table_raw = excel_data.sheets()[0]
    ncols = table_raw.ncols
    nrows = table_raw.nrows
    tables = table_raw.row_values(xl)
    tits = str(tables[0])
    return tits


def row_base(T, xh, xs, xe):
    excel_data = xr.open_workbook(str(filename))
    table_raw = excel_data.sheets()[0]
    ncols = table_raw.ncols
    nrows = table_raw.nrows
    axisline = table_raw.row_values(0)
    initial = 0
    final = len(axisline) - xh
    for i in range(len(axisline) - xh):
        a0 = axisline[i + xh]
        d0 = abs(axisline[xh + 2] - axisline[xh + 1])
        if abs(xs - a0) <= d0/2.0:
            initial = i
        if abs(xe - a0) <= d0/2.0:
            final = i
        else:
            continue
    base = T[initial:final]
    return base


def updator():
    if os.path.exists('name.txt'):
        os.remove('name.txt')


def main():
    if dim == 'cols':
        excel_data = xr.open_workbook(str(filename))
        table_raw = excel_data.sheets()[0]
        ncols = table_raw.ncols
        nrows = table_raw.nrows
        X0 = col_selector(0, header)
        Y0 = col_selector(pbs, header)
        Y1 = col_selector(line_number, header)
        X2 = col_base(X0, header, start, end)
        Y2 = col_base(Y1, header, start, end)
        np.savetxt('baseline_X_'+str(parts)+'.csv', X2, delimiter=',')
        np.savetxt('baseline_Y_'+str(parts)+'.csv', Y2, delimiter=',')
        np.savetxt('curve_X.csv', X0, delimiter=',')
        np.savetxt('curve_Y.csv', Y1, delimiter=',')
        f = open('name.txt', 'a')
        f.write(col_title(line_number))
        f.close()
        plt.figure()
        l1, = plt.plot(X0, Y0, color='black')
        l2, = plt.plot(X0, Y1, color='pink', linestyle='--')
        l3, = plt.plot(X2, Y2, color='red')
        plt.legend(handles=[l1, l2, l3], labels=['background', 'curve', 'chosen part'])
        plt.xlabel('potential/V')
        plt.ylabel(r'$\Delta I / \mu A$')
        plt.savefig('temporary.pdf')
        plt.show()
    if dim == 'rows':
        excel_data = xr.open_workbook(str(filename))
        table_raw = excel_data.sheets()[0]
        ncols = table_raw.ncols
        nrows = table_raw.nrows
        X0 = row_selector(0, header)
        Y0 = row_selector(pbs, header)
        Y1 = row_selector(line_number, header)
        X2 = row_base(X0, header, start, end)
        Y2 = row_base(Y1, header, start, end)
        np.savetxt('baseline_X_'+str(parts)+'.csv', X2, delimiter=',')
        np.savetxt('baseline_Y_'+str(parts)+'.csv', Y2, delimiter=',')
        np.savetxt('curve_X.csv', X0, delimiter=',')
        np.savetxt('curve_Y.csv', Y1, delimiter=',')
        f = open('name.txt', 'a')
        f.write(col_title(line_number))
        f.close()
        plt.figure()
        l1, = plt.plot(X0, Y0, color='black')
        l2, = plt.plot(X0, Y1, color='pink', linestyle='--')
        l3, = plt.plot(X2, Y2, color='red')
        plt.legend(handles=[l1, l2, l3], labels=['background', 'curve', 'chosen part'])
        plt.xlabel('potential/V')
        plt.ylabel(r'$\Delta I / \mu A$')
        plt.savefig('temporary.pdf')
        plt.show()


####################
def begin():
    updator()
    main()


b_s = tk.Button(root, text='draw', command=begin)
b_s.place(x=16, y=304, width=160, height=32)
####################
####################
varsa = tk.StringVar()
e_sa = tk.Entry(root, textvariable=varsa)
varsa.set('total segments')
e_sa.place(x=16, y=336, width=160, height=32)


def shows():
    global stages
    stages = int(varsa.get().strip())


b_3 = tk.Button(root, text='fix baseline', command=shows)
b_3.place(x=16, y=368, width=160, height=32)

basepoints_Y = []
basepoints_X = []


def base_list_x(xp):
    matrix = np.loadtxt(open('baseline_X_'+str(xp)+'.csv', 'rb'), delimiter=',', skiprows=0)
    return matrix


def base_list_y(xp):
    matrix = np.loadtxt(open('baseline_Y_'+str(xp)+'.csv', 'rb'), delimiter=',', skiprows=0)
    return matrix


def curve_list_x():
    matrix = np.loadtxt(open('curve_X.csv', 'rb'), delimiter=',', skiprows=0)
    return matrix


def curve_list_y():
    matrix = np.loadtxt(open('curve_Y.csv', 'rb'), delimiter=',', skiprows=0)
    return matrix


def conpound():
    for pi in range(stages):
        for ti in range(len(base_list_x(pi + 1))):
            valuex = base_list_x(pi + 1)
            basepoints_X.append(valuex[ti])
    for pi in range(stages):
        for ti in range(len(base_list_y(pi + 1))):
            valuey = base_list_y(pi + 1)
            basepoints_Y.append(valuey[ti])


def bubble():
    global basepoints_X, basepoints_Y
    for i in range(len(basepoints_X) - 1):
        for j in range(len(basepoints_X) - 1 - i):
            if basepoints_X[j] > basepoints_X[j + 1]:
                a = basepoints_X[j]
                b = basepoints_X[j + 1]
                ay = basepoints_Y[j]
                by = basepoints_Y[j + 1]
                basepoints_X[j] = b
                basepoints_X[j + 1] = a
                basepoints_Y[j] = by
                basepoints_Y[j + 1] = ay
            else:
                continue


def main_2():
    conpound()
    bubble()
    x_new = curve_list_x()
    tck = interpolate.splrep(basepoints_X, basepoints_Y)
    y_b = interpolate.splev(x_new, tck)
    y_new = curve_list_y() - y_b
    f = open('name.txt')
    fcon = f.read()
    f.close()
    np.savetxt(str(fcon)+'_curve_X.csv', x_new, delimiter=',')
    np.savetxt(str(fcon)+'_curve_Y.csv', y_new, delimiter=',')
    plt.figure()
    plt.plot(x_new, y_new, color='red', linewidth=2.0)
    plt.xlabel('potential/V')
    plt.ylabel(r'$\Delta I / \mu A$')
    plt.title(str(fcon)+' curve after subtracted baseline')
    plt.savefig(str(fcon)+' curve after subtracted baseline.pdf')
    plt.show()


b_4 = tk.Button(root, text='show', command=main_2)
b_4.place(x=16, y=400, width=160, height=32)


def refresh():
    global basepoints_X, basepoints_Y
    basepoints_Y = []
    basepoints_X = []


b_re = tk.Button(root, text='refresh', command=refresh)
b_re.place(x=16, y=432, width=160, height=32)
####################
vartf = tk.StringVar()
e_tf = tk.Entry(root, textvariable=vartf)
vartf.set('name of final figure')
e_tf.place(x=336, y=16, width=160, height=32)

varxl1 = tk.StringVar()
e_xl1 = tk.Entry(root, textvariable=varxl1)
varxl1.set('lower limit of x axis')
e_xl1.place(x=336, y=48, width=160, height=32)

varxl2 = tk.StringVar()
e_xl2 = tk.Entry(root, textvariable=varxl2)
varxl2.set('upper limit of x axis')
e_xl2.place(x=336, y=80, width=160, height=32)

varyl1 = tk.StringVar()
e_yl1 = tk.Entry(root, textvariable=varyl1)
varyl1.set('lower limit of y axis')
e_yl1.place(x=336, y=112, width=160, height=32)

varyl2 = tk.StringVar()
e_yl2 = tk.Entry(root, textvariable=varyl2)
varyl2.set('upper limit of y axis')
e_yl2.place(x=336, y=144, width=160, height=32)


def main_3():
    global figurename, xlim1, xlim2, ylim1, ylim2
    figurename = str(vartf.get().strip())
    xlim1 = float(varxl1.get().strip())
    xlim2 = float(varxl2.get().strip())
    ylim1 = float(varyl1.get().strip())
    ylim2 = float(varyl2.get().strip())
    colortable = ['black', 'brown', 'red', 'chocolate', 'darkorange', 'gold', 'lawngreen', 'seagreen', 'darkcyan', 'slategray', 'blue', 'purple', 'deeppink']
    excel_data = xr.open_workbook(str(filename))
    table_raw = excel_data.sheets()[0]
    ncols = table_raw.ncols
    nrows = table_raw.nrows
    if dim == 'cols':
        pic_object = []
        label_object = []
        plt.figure()
        for i in range(ncols - 1):
            if os.path.exists(col_title(i + 1)+'_curve_X.csv'):
                matrixoX = np.loadtxt(open(col_title(i + 1)+'_curve_X.csv'), delimiter=",", skiprows=0)
                matrixoY = np.loadtxt(open(col_title(i + 1)+'_curve_Y.csv'), delimiter=",", skiprows=0)
                plt.subplot(1, 1, 1)
                li, = plt.plot(matrixoX, matrixoY, color=colortable[i], linewidth=2.0)
                pic_object.append(li)
                label_object.append(col_title(i + 1))
            else:
                continue
        plt.xlabel('potential/V')
        plt.ylabel(r'$\Delta I / \mu A$')
        plt.title(str(figurename))
        plt.xlim(xlim1, xlim2)
        plt.ylim(ylim1, ylim2)
        plt.legend(pic_object, label_object, loc='best')
        plt.savefig('result.pdf')
        plt.show()
    if dim == 'rows':
        pic_object = []
        label_object = []
        plt.figure()
        for i in range(nrows - 1):
            if os.path.exists(row_title(i + 1)+'_curve_X.csv'):
                matrixoX = np.loadtxt(open(col_title(i + 1)+'_curve_X.csv'), delimiter=",", skiprows=0)
                matrixoY = np.loadtxt(open(col_title(i + 1)+'_curve_Y.csv'), delimiter=",", skiprows=0)
                plt.subplot(1, 1, 1)
                li, = plt.plot(matrixoX, matrixoY, color=colortable[i], linewidth=2.0)
                pic_object.append(li)
                label_object.append(row_title(i + 1))
            else:
                continue
        plt.xlabel('potential/V')
        plt.ylabel(r'$\Delta I / \mu A$')
        plt.title(str(figurename))
        plt.xlim(xlim1, xlim2)
        plt.ylim(ylim1, ylim2)
        plt.title(str(figurename))
        plt.legend(pic_object, label_object, loc='best')
        plt.savefig('result.pdf')
        plt.show()


b_5 = tk.Button(root, text='conclusion', command=main_3)
b_5.place(x=336, y=176, width=160, height=32)


def original_main():
    global figurename, xlim1, xlim2, line_number, ylim1, ylim2
    figurename = str(vartf.get().strip())
    xlim1 = float(varxl1.get().strip())
    xlim2 = float(varxl2.get().strip())
    ylim1 = float(varyl1.get().strip())
    ylim2 = float(varyl2.get().strip())
    colortable = ['black', 'brown', 'red', 'chocolate', 'darkorange', 'gold', 'lawngreen', 'seagreen', 'darkcyan', 'slategray', 'blue', 'purple', 'deeppink']
    excel_data = xr.open_workbook(str(filename))
    table_raw = excel_data.sheets()[0]
    ncols = table_raw.ncols
    nrows = table_raw.nrows
    if dim == 'cols':
        pic_object = []
        label_object = []
        plt.figure()
        for i in range(ncols - 1):
            if os.path.exists(col_title(i + 1)+'_curve_X.csv'):
                matrixoX2 = col_selector(0, header)
                matrixoY2 = col_selector(i + 1, header)
                plt.subplot(1, 1, 1)
                li, = plt.plot(matrixoX2, matrixoY2, color=colortable[i], linewidth=2.0)
                pic_object.append(li)
                label_object.append(col_title(i + 1))
            else:
                continue
        plt.xlabel('potential/V')
        plt.ylabel(r'$\Delta I / \mu A$')
        plt.title('raw curve of '+str(figurename))
        plt.xlim(xlim1, xlim2)
        plt.ylim(ylim1, ylim2)
        plt.legend(pic_object, label_object, loc='best')
        plt.savefig('result_r.pdf')
        plt.show()
    if dim == 'rows':
        pic_object = []
        label_object = []
        plt.figure()
        for i in range(nrows - 1):
            if os.path.exists(row_title(i + 1)+'_curve_X.csv'):
                matrixoX2 = row_selector(0, header)
                matrixoY2 = row_selector(i + 1, header)
                plt.subplot(1, 1, 1)
                li, = plt.plot(matrixoX2, matrixoY2, color=colortable[i], linewidth=2.0)
                pic_object.append(li)
                label_object.append(col_title(i + 1))
            else:
                continue
        plt.xlabel('potential/V')
        plt.ylabel(r'$\Delta I / \mu A$')
        plt.title('raw curve of '+str(figurename))
        plt.xlim(xlim1, xlim2)
        plt.ylim(ylim1, ylim2)
        plt.legend(pic_object, label_object, loc='best')
        plt.savefig('result_r.pdf')
        plt.show()


b_6 = tk.Button(root, text='raw curve', command=original_main)
b_6.place(x=336, y=208, width=160, height=32)
####################
root.mainloop()
####################
