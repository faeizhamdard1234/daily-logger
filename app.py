import click

@click.command
@click.argument('name')
@click.argument('age')
@click.option('--greet' , default="Helo" , help="this is for greeting")
@click.option('--repeat' , default= 1 ,type=click.IntRange(min=1) , help="how many repeat ")
@click.option('--shout' , is_flag=True , help="be upper")

def hello (name , age , greet , repeat , shout):
    if shout :
        name=name.upper() 
        name_color = click.style(name ,fg="red")
    greet_color = click.style(greet , fg="green" , bg="yellow" , bold=True)
    
    for i in range(repeat):
        click.echo(f"your name is {name_color} and your age is {age}")
        
if __name__ == '__main__' :
    hello()
