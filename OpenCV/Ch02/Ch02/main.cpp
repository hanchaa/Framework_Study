#include "opencv2/opencv.hpp"
#include <iostream>

using namespace std;
using namespace cv;

int main() {
	cout << "Hello OpenCV" << CV_VERSION << endl;

	Mat img = imread("lenna.bmp");

	if (img.empty()) {
		cerr << "Image load failed!" << endl;
		return -1;
	}
	
	namedWindow("image");
	imshow("image", img);

	waitKey();


	return 0;
}