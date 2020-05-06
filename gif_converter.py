import imageio
import os

clip = os.path.abspath('video.mp4')


def gifMaker(inputpath, targetFormat):
	outputpath = os.path.splitext(inputpath)[0] + targetFormat

	print(f'converting {inputpath} \n to {outputpath}')

	reader = imageio.get_reader(inputpath)
	fps = reader.get_meta_data()['fps']

	writer = imageio.get_writer(outputpath,fps=fps)

	for frames in reader:
		writer.append_data(frames)
		print(f'Frame {frames}')
	
	print("Done!")
	writer.close()


gifMaker(clip,'.gif')
