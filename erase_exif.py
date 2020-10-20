'''
Erase EXIF information from images using PIL.

author : STomoya (https://github.com/STomoya)
'''

import os
import warnings
from PIL import Image

def erase_exif(image_path, dst_path):
    '''
    erases exif using PIL.

    args
        image_path: str
            the path of the source image
        dst_path: str
            the path of the destination image
    '''
    with Image.open(image_path) as image:
        data = image.getdata()
        mode = image.mode
        size = image.size
    with Image.new(mode, size) as dst:
        dst.putdata(data)
        dst.save(dst_path)

def erase_corrupt_exif(image_paths, keep_image=False, verbose=False):
    '''
    only erase exif of images with corrupt exif.
    fast but file size would not change.

    args
        image_paths: [str]
            list of path to images in str
        keep_image: bool (default:False)
            if True, a new image will be made instead of overwriting the file

    ret
        past_files: [str]
            list of files that still exists but has corrupt exif
    '''
    assert isinstance(image_paths, list) and isinstance(image_paths[0], str), 'src_paths must be a list of strings.'

    # make warnings catchable
    warnings.filterwarnings('error')

    past_files = []
    for image_path in image_paths:
        try:
            with Image.open(image_path) as tmp:
                pass
        except Exception as e:
            # show warnings
            print(e)
            if keep_image:
                # keep track of source file
                past_files.append(image_path)
                # create new filename
                path_particles = image_path.split('.')
                suffix = path_particles[-1]
                dir_and_stem = path_particles[0] if len(path_particles) == 2 else '.'.join(path_particles[:-1])
                dir_and_stem += '_no_exif'
                dst_path = '.'.join([dir_and_stem, suffix])
            else:
                # overwrite file
                dst_path = image_path
            if verbose:
                print(f'\'{image_path}\' will be saved to \'{dst_path}\' with no exif.')
            with warnings.catch_warnings():
                warnings.filterwarnings('ignore')
                erase_exif(image_path, dst_path)
    
    if len(past_files) > 0:
        print('files with corrupt exif')
        print(past_files)
    return past_files

def erase_all_exif(image_paths, keep_image=False, verbose=False):
    '''
    erase exif of all images in image_paths
    slow but decreases image file size better.

    args
        image_paths: [str]
            list of path to images in str
        keep_image: bool (default:False)
            if True, a new image will be made instead of overwriting the file
    '''
    assert isinstance(image_paths, list) and isinstance(image_paths[0], str), 'src_paths must be a list of strings.'

    for image_path in image_paths:
        if keep_image:
            # create new filename
            path_particles = image_path.split('.')
            suffix = path_particles[-1]
            dir_and_stem = path_particles[0] if len(path_particles) == 2 else '.'.join(path_particles[:-1])
            dir_and_stem += '_no_exif'
            dst_path = '.'.join([dir_and_stem, suffix])
        else:
            # overwrite file
            dst_path = image_path
        if verbose:
            print(f'\'{image_path}\' will be saved to \'{dst_path}\' with no exif.')
        erase_exif(image_path, dst_path)