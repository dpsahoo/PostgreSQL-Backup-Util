from argparse import Action, ArgumentParser

class DriverAction(Action):
	def __call__(self, parser, namespace, values, option_string=None):
		driver, destination = values
		namespace.driver = driver
		namespace.destination = destination



def create_parser():
	parser = ArgumentParser(description="""
		Backup PostgreSQL databases locally or to AWS S3.
		""")
	parser.add_argument("url", help="URL of database to backup")
	parser.add_argument("--driver",
		help="how and where to store the database backup",
		nargs=2,
		action=DriverAction,
		required=True)
	return parser


def main():
	import boto3
	from pgbackup import pgdump, storage

	args = create_parser().parse_args()
	dump = pgdump.dump(args.url)
	if args.driver == 's3':
		client = boto3.client('s3')
		storage.s3(client, dump.stdout, args.destination, 'example.sql')
	else:
		outfile = open(args.destination, 'wb')
		storage.local(dump.stdout, outfile)	



	


