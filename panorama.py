import sys, os, pathlib, datetime, cv2
import image_stitching.read_images as read_images
import image_stitching.recursion  as recursion


def main(image_dir_list, tag):

    images_list, n_imgs = read_images.read(image_dir_list)
    result, mapped_image = recursion.recurse(images_list, n_imgs)

    out_dir = pathlib.Path("outputs") / tag           
    out_dir.mkdir(parents=True, exist_ok=True)

    cv2.imwrite(str(out_dir / "panorama.jpg"), result)
    cv2.imwrite(str(out_dir / "mapped.jpg"),   mapped_image)
    print(f"Saved to {out_dir}/")


if __name__ == "__main__":
    cli_args = sys.argv[1:]

    if len(cli_args) == 1 and os.path.isdir(cli_args[0]):
        folder = pathlib.Path(cli_args[0])
        img_paths = sorted(folder.glob("*.[jJ][pP]*g"))
        if not img_paths:
            raise FileNotFoundError(f"No images found in {folder}")
        image_list = [str(p) for p in img_paths]

        run_tag = folder.name                        
    else:
        image_list = cli_args
        if not image_list:
            raise ValueError("Give either a folder or image paths, e.g.\n"
                             "   python panorama.py inputs/front/\n"
                             "   python panorama.py img1.jpg img2.jpg ...")
        # derive a tag from first file or use timestamp
        run_tag = pathlib.Path(image_list[0]).stem.split('_')[0] \
                  or datetime.datetime.now().strftime("%Y%m%d_%H%M%S")  

    print("Images that will be stitched (in order):")
    for p in image_list:
        print("  ", p)

    main(image_list, run_tag)
