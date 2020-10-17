# erase exif

Python code for erasing EXIF information from image files.  
Some images, especially ones scraped from Internet, has corrupt EXIF information.

## Requirements

- pillow

## Usage

- Single image.

```python
    from erase_exif import erase_exif
    src_path = 'path/to/image.jpg'
    dst_path = 'path/to/destination.jpg'
    erase_exif(src_path, dst_path)
```

- Multiple images.

    - All images in a list

        Slow but reduces the file size more.

    ```python
    from erase_exif import erase_all_exif

    # src_paths sould be a list of str
    # example
    src_paths = ['path/to/image00.jpg', 'path/to/image01.jpg', ...]
    # or
    import glob
    src_paths = glob.glob('path/to/image/folder/*')
    # or
    from pathlib import Path
    src_paths = Path('path/to/image/folder').glob('*')
    src_paths = [str(path) for path in src_paths]

    # erase all EXIF
    erase_all_exif(src_paths)
    # or if you want to keep the images
    # If the filename is 'image.jpg', the file with no EXIF info will be 'image_no_exif.jpg'
    erase_all_exif(src_paths, keep_images=True)
    ```

    - Erase only corrupt EXIF.

        Fast, but does not reduce file size.

    ```python
    from erase_exif import erase_corrupt_exif

    # src_paths should be a list of str
    # examples are in codes above
    src_paths = ['path/to/image00.jpg', 'path/to/image01.jpg', ...]

    # erase only corrupt EXIF
    erase_corrupt_exif(src_paths)
    # or if you want to keep the images
    # If the filename is 'image.jpg', the file with no EXIF info will be 'image_no_exif.jpg'
    # This will return a list of filenames with corrupt EXIF info if exists.
    # Use this to eliminate them when using the files.
    past_files = erase_corrupt_exif(src_paths, keep_images=True)
    ```

## Author

[STomoya](https://github/com/STomoya)
