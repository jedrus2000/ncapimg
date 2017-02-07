# -*- coding: utf-8 -*-
import subprocess
import urllib.request
import os


def run_rurl(base_url, image_id, max_cols, max_rows):
    """
    Runs curl to download images.

    base_url - base URL of image i.e.: http://ncap.org.uk/sites/all/libraries/zoomify512/
    image_id - image id, i.e.: NCAP-000-000-035-852
    max_cols - integer
    max_rows - integer
    """

    # create directory for image
    try:
        os.makedirs(image_id)
    except OSError:
        pass

    found_rows, found_cols = -1, -1

    image_url_arr = image_id.split('-')

    # download tiles
    for y in range(0, max_rows):
        for x in range(0, max_cols):
            # download file
            url = "%s%s/%s/%s/%s/TileGroup0/3-%d-%d.jpg" % (base_url, image_url_arr[1],
                                                            image_url_arr[2], image_url_arr[3], image_id, x, y)
            # print(url)
            try:
                print("Downloading: %s " % url)
                urllib.request.urlretrieve(url, os.path.join(image_id, "tile_row%02d_column%02d.jpg" % (y, x)))
                if x > found_cols:
                    found_cols = x
                if y > found_rows:
                    found_rows = y
                print("Ok")
            except urllib.error.HTTPError as e:
                print("HTTP Error: %s" % e.code)
                # print(e.read())

    # join files
    found_rows += 1
    found_cols += 1
    # print("found_cols=%s found_rows=%s" % (found_cols, found_rows))

    if found_rows > 0 and found_cols > 0:
        subprocess.call(["montage", "-mode", "concatenate", "-tile", "%dx%d" % (found_cols, found_rows),
                         os.path.join(image_id, "tile_*.jpg"), os.path.join(image_id, "final_image.jpg")])
        print("Finished !")
    else:
        print("Images not found")


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description="Downloads zoomify tiles and creates image.\n"
                    "Project page at: https://github.com/jedrus2000/ncapimg",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("image_id", help="image id string, i.e.: NCAP-000-000-302-950")
    parser.add_argument("-main_url", help="main NCAP url", default="http://ncap.org.uk/sites/all/libraries/zoomify512/")
    parser.add_argument("-columns", help="image tiles: number of columns", type=int, default=9)
    parser.add_argument("-rows", help="image tiles: number of rows", type=int, default=9)
    args = parser.parse_args()

    run_rurl(args.main_url, args.image_id, args.columns, args.rows)

