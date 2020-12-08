import argparse
import cv2


def main():
    parser = argparse.ArgumentParser(description='Boarder Calibration.')
    parser.add_argument('input_EPM_path', help='Path of edge probaiblity map.')
    parser.add_argument('input_boarder_path', help='Path of boarder mask.')
    parser.add_argument('output_path', help='Path of update boader image.')

    args = parser.parse_args()

    EPM = cv2.imread(args.input_EPM_path, cv2.IMREAD_GRAYSCALE)
    BOD = cv2.imread(args.input_boarder_path, cv2.IMREAD_GRAYSCALE)

    # for each pixel p(x,y) where value = 0 in the mask, you should set the
    # EPM pixel p(x,y) to 0 (sure no edge)
    # for p(x,y) = 255 in mask: set p(x,y) = 255 in EPM (sure edge)
    # for p(x,y) = 128 in mask: keep p(x,y) original value in EPM.
    #EPM[BOD == 0] = 0
    #EPM[BOD == 255] = 255
    res = cv2.bitwise_and(EPM,EPM,mask = BOD)
    cv2.imwrite(args.output_path, res)
    print('Save calibration results to {}'.format(args.output_path))

if __name__ == '__main__':
    main()
