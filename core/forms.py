from django import forms
from django.core.mail.message import EmailMessage


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    telefone = forms.CharField(label='Telefone', max_length=20)
    mensagem = forms.CharField(label='Mensagem',
                               widget=forms.Textarea())
    # mensagem = forms.Textarea()

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        telefone = self.cleaned_data['telefone']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'De: {nome}\n {mensagem}\n Telefone: {telefone}'

        mail = EmailMessage(
            subject=f'Contato de {nome}',
            body=conteudo,
            from_email=email,
            to=['contato@fabricasites.com.br'],
            headers={'Reply_To': email}
        )
        mail.send()