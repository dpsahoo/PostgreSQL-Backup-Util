def test_durga():
	printf('test_durga')	

#Define local storage function
def local(infile, outfile):
	outfile.write(infile.read())
	outfile.close()
	infile.close()

#Define AWS S3 storage function
def s3(client, infile, bucket, name):
	client.upload_fileobj(infile, bucket, name)

