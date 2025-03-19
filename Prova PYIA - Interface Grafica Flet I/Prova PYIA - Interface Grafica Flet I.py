import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    tarefas = ft.Column()

    input_tarefa = ft.TextField(label="Digite uma tarefa")
    
    def adicionar_tarefa(e):
        if input_tarefa.value:
            tarefas.controls.append(ft.Text(input_tarefa.value))
            input_tarefa.value = ""
            page.update()
    
    botao_adicionar = ft.ElevatedButton("Adicionar", on_click=adicionar_tarefa)
    
    page.add(input_tarefa, botao_adicionar, tarefas)

ft.app(target=main)
