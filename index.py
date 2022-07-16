from tkinter import*
import sys
import csv
from tkinter import messagebox
from tkinter import ttk
from tkinter.tix import Tree
from tkinter import ttk
from tkinter.tix import Tree
from dados import *
 
cor_cinza="#f0f3f5"
cor_branca="#feffff"
cor_verde="#3fb5a3"
cor_preta="#2e2d2c"
cor_azul="#4a88e8"
cor_letra="#403d3d"
cor_vermelha="#ef5350"
cor_verde="#93cd95"
cor_azul_tela="#38576b"


janela=Tk()
janela.title("")
janela.geometry("500x450")
janela.configure(background=cor_cinza)
janela.resizable(width=False,height=False)





frame_cima=Frame(janela,width=500,height=50,bg=cor_azul_tela,relief='flat')
frame_cima.grid(row=0,column=0,pady=1,padx=0,sticky=NSEW)

frame_baixo=Frame(janela,width=500,height=150,bg=cor_cinza,relief='flat')
frame_baixo.grid(row=1,column=0,pady=1,padx=0,sticky=NSEW)

frame_tabela=Frame(janela,width=500,height=248,bg=cor_branca,relief='flat')
frame_tabela.grid(row=2,column=0,columnspan=2,pady=10,padx=1,sticky=NSEW)

#estilizando frame cima

label__nome=Label(frame_cima,text="Agenda Telefónica",anchor=NE,font=('arial 20 bold'), bg=cor_azul_tela,fg=cor_branca)
label__nome.place(x=5,y=5)

label__linha=Label(frame_cima,width=500,anchor=NE,font=('arial 1'), bg=cor_branca)
label__linha.place(x=0,y=46)





global tree

def  mostrar_dados():
    
        global tree

        #configurando frame ta
        dados_h=['Nome','Sexo','Telefone','Email']
                
        dados=ver_dados()
                
                
        tree= ttk.Treeview(frame_tabela,selectmode="extended",columns=dados_h,show="headings")
                
        vsb=ttk.Scrollbar(
        frame_tabela,orient="vertical",command=tree.yview )
                
        hsb=ttk.Scrollbar(
            frame_tabela,orient="horizontal",command=tree.xview )

        tree.configure(yscrollcommand=vsb.set,xscrollcommand=hsb.set)
                
        tree.grid(column=0,row=0,sticky='nsew')
        vsb.grid(column=1,row=0,sticky='ns')
        hsb.grid(column=0,row=1,sticky='ew')
                
            
            
        tree.heading(0,text='Nome',anchor=NW)
        tree.heading(1,text='Sexo',anchor=NW)
        tree.heading(2,text='Telefone',anchor=NW)
        tree.heading(3,text='Email',anchor=NW)
                
        tree.column(0,width=120,anchor='nw')
        tree.column(1,width=50,anchor='nw')
        tree.column(2,width=100,anchor='nw')
        tree.column(0,width=120,anchor='nw')
                
        for item in dados:
            tree.insert('','end',values=item)


mostrar_dados()


#funcao inserir

def inserir():
    nome=entry_nome.get()
    sexo=entry_sexo.get()
    telefone=entry_telefone.get()
    email=entry_email.get()
    
    
    dados=[nome,sexo,telefone,email]
    
    if nome == '' or sexo=='' or telefone=='' or email=='':
        messagebox.showwarning('Dados','Por favor preencha todos os campos')
    else:
        adicicionar_dados(dados)
        messagebox.showinfo('Dados','Os dados foram adicionados com sucesso')
        entry_nome.delete(0,'end')
        entry_sexo.delete(0,'end')
        entry_telefone.delete(0,'end')
        entry_email.delete(0,'end')
        
        mostrar_dados()

def  atualizar():
    try:
        treev_dados=tree.focus()
        treev_dicionario=tree.item(treev_dados)
        tree_lista=treev_dicionario['values']
        
        nome=tree_lista[0]
        sexo=tree_lista[1]
        telefone=str(tree_lista[2])
        email=tree_lista[3]
        
        
        entry_nome.insert(0,nome)
        entry_sexo.insert(0,sexo)
        entry_telefone.insert(0,telefone)
        entry_email.insert(0,email)
        
            
        def confirmar():
                nome=entry_nome.get()
                sexo=entry_sexo.get()
                telefone_novo=entry_telefone.get()
                email=entry_email.get()
                
                
                dados=[telefone,nome,sexo,telefone_novo,email]
                
                
                print(dados)
                
                atualizar_dados(dados)
                
            
                messagebox.showinfo('Dados','Os dados foram atualizados com sucesso')
                entry_nome.delete(0,'end')
                entry_sexo.delete(0,'end')
                entry_telefone.delete(0,'end')
                entry_email.delete(0,'end')
                
                
                b__confirmar.destroy()
                
                mostrar_dados()
        b__confirmar=Button(frame_baixo,command=confirmar,text="Confirmar",width=10,font=('Ivy 8 bold '), bg=cor_branca,fg=cor_letra, relief=RAISED ,overrelief=RIDGE)
        b__confirmar.place(x=290,y=110)  
        
    except:
        messagebox.showwarning('Dados','Selecione uma informação na tabela')
    

def remover():
    try:
        treev_dados=tree.focus()
        treev_dicionario=tree.item(treev_dados)
        tree_lista=treev_dicionario['values']
        
        telefone=str(tree_lista[2])
        
        remover_dados(telefone)
        
        
        messagebox.showinfo('Dados','Os dados foram deletados com sucesso')
        
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        
        mostrar_dados()
            
    except:
        messagebox.showwarning('Dados','Selecione uma informação na tabela')
    
def  procurar():
    telefone=entry_procurar.get()
    
    dados=pesquisar_dados(telefone) 
    
    tree.delete(*tree.get_children())
    
    for item in dados:
        tree.insert('','end',values=item)
        
    entry_procurar.delete(0,'end')
    
    

#estilizando frame baixo

label__nome=Label(frame_baixo,text="Nome *",anchor=NW,font=('Ivy 10 '), bg=cor_cinza,fg=cor_letra)
label__nome.place(x=10,y=20)
entry_nome=Entry(frame_baixo,width=25,justify='left',font=('',10),highlightthickness=1)
entry_nome.place(x=80,y=20)

label__sexo=Label(frame_baixo,text="Sexo *",anchor=NW,font=('Ivy 10 '), bg=cor_cinza,fg=cor_letra)
label__sexo.place(x=10,y=50)
entry_sexo=Entry(frame_baixo,width=25,justify='left',font=('',10),highlightthickness=1)
entry_sexo.place(x=80,y=50)

label__telefone=Label(frame_baixo,text="Telefone *",anchor=NW,font=('Ivy 10 '), bg=cor_cinza,fg=cor_letra)
label__telefone.place(x=10,y=80)
entry_telefone=Entry(frame_baixo,width=25,justify='left',font=('',10),highlightthickness=1)
entry_telefone.place(x=80,y=80)

label__email=Label(frame_baixo,text="Email *",anchor=NW,font=('Ivy 10 '), bg=cor_cinza,fg=cor_letra)
label__email.place(x=10,y=110)
entry_email=Entry(frame_baixo,width=25,justify='left',font=('',10),highlightthickness=1)
entry_email.place(x=80,y=110)


b__procurar=Button(frame_baixo,command=procurar,text="Buscar",font=('Ivy 8 bold '), bg=cor_cinza,fg=cor_letra, relief=RAISED ,overrelief=RIDGE)
b__procurar.place(x=290,y=20)
entry_procurar=Entry(frame_baixo,width=16,justify='left',relief='flat',font=('',11),highlightthickness=1)
entry_procurar.place(x=347,y=21)

b__verdados=Button(frame_baixo,command=mostrar_dados,text="Ver dados",width=10,font=('Ivy 8 bold '), bg=cor_branca,fg=cor_letra, relief=RAISED ,overrelief=RIDGE)
b__verdados.place(x=290,y=50)

b__adicionar=Button(frame_baixo,command=inserir,text="Adiconar",width=10,font=('Ivy 8 bold '), bg=cor_branca,fg=cor_letra, relief=RAISED ,overrelief=RIDGE)
b__adicionar.place(x=400,y=50)

b__atualizar=Button(frame_baixo,command=atualizar,text="Atualizar",width=10,font=('Ivy 8 bold '), bg=cor_verde,fg=cor_letra, relief=RAISED ,overrelief=RIDGE)
b__atualizar.place(x=400,y=80)

b__deletar=Button(frame_baixo,command=remover,text="Deletar",width=10,font=('Ivy 8 bold '), bg=cor_vermelha,fg=cor_letra, relief=RAISED ,overrelief=RIDGE)
b__deletar.place(x=400,y=110)




janela.mainloop()