from django.core.management import BaseCommand
from slack.webhook.client import WebhookClient
 
class Command(BaseCommand):
    help = 'Webhook連携チャンネルにメッセージを投稿する'
    def add_arguments(self, parser):
        parser.add_argument('--opt', help='任意オプション')
 
    def handle(self, *args, **options):
        url = "xxxx" #対象チャンネルのWebhookURLを入力する  
        client = WebhookClient(url=url)
        client.send(text="django message test")
        

        #self.stdout.write(self.style.SUCCESS('Hello Django Command!'))
        #self.stdout.write(options.__str__())
