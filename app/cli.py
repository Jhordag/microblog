from app import app
import click
import os



def register(app):
    @app.cli.group()
    def translate():
        pass
    @translate.command()
    @click.argument('lang')
    def init(lang):
        if os.system('pylabel extract -F babel.cfg -k -l -o messages.po .'):
            raise RuntimeError('extract command failed')
        
        if os.system(
            'pylabel init -i messages.pos -d app/translations -l' + lang):
            raise RuntimeError('init command failed')
        
        os.remove('messages.port')
        
    @translate.command()
    def update():
        if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
            raise RuntimeError('extract command failed')
        if os.system('pybabel update -i messages.pot -d app/translations'):
            raise RuntimeError('update command failed')
        os.remove('messages.pot')

    @translate.command()
    def compile():
        if os.system(
            'pybabel compile -d app/translations'):
            raise RuntimeError('complite command failed')
