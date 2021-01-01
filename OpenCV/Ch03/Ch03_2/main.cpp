#include "opencv2/opencv.hpp"
#include <iostream>

using namespace std;
using namespace cv;

int main() {
	
	//Mat 클래스
	{
		cout << "Mat 클래스" << endl;

		Mat img1(480, 640, CV_8UC1);
		Mat img2(480, 640, CV_8UC3);
		Mat img3(Size(640, 480), CV_8UC3);

		Mat img4(480, 640, CV_8UC1, Scalar(128));
		Mat img5(480, 640, CV_8UC3, Scalar(0, 0, 255));
	}

	{
		Mat mat1 = Mat::zeros(3, 3, CV_32SC1);
		Mat mat2 = Mat::ones(3, 3, CV_32FC1);
		Mat mat3 = Mat::eye(3, 3, CV_32FC1);

		cout << "Mat3" << endl << mat3 << endl;

		float data[] = { 1, 2, 3, 4, 5, 6 };
		Mat mat4(2, 3, CV_32FC1, data);

		cout << "Mat4" << endl << mat4 << endl;

		Mat mat5 = (Mat_<float>(2, 3) << 1, 2, 3, 4, 5, 6);
		Mat mat6 = Mat_<float>({ 2, 3 }, { 1, 2, 3, 4, 5, 6 });

		mat4.create(256, 256, CV_8UC3);
		mat5.create(4, 4, CV_32FC1);

		mat4 = Scalar(255, 0, 0);
		mat5.setTo(1.f);

		imshow("Mat4", mat4);
		waitKey();

		destroyWindow("Mat4");

		cout << "Mat5" << endl << mat5 << endl << endl;
	}

	//행렬의 복사
	{
		Mat img1 = imread("dog.bmp");
		Mat img2 = img1;

		Mat img3;
		img3 = img1; // 얕은 복사, 메모리 주소 공유

		Mat img4 = img1.clone();
		Mat img5;
		img1.copyTo(img5); // 깊은 복사, 메모리 주소 공유 x

		img1.setTo(Scalar(0, 255, 255));

		imshow("Img1", img1);
		imshow("Img2", img2);
		imshow("Img3", img3);
		imshow("Img4", img4);
		imshow("Img5", img5);

		waitKey();
		destroyAllWindows();
	}

	//부분 행렬 추출
	{
		Mat img1 = imread("cat.bmp");

		if (img1.empty()) {
			cerr << "Image load failed!" << endl;
			return 0;
		}

		//Mat img2 = img1(Rect(220, 120, 340, 240));
		Mat img2 = img1(Range(120, 360), Range(220, 560)); // 얕은 복사
		Mat img3 = img1(Rect(220, 120, 340, 240)).clone();

		Mat img4 = img1.rowRange(120, 360);
		Mat img5 = img1.colRange(220, 560);
		
		Mat img6 = img1.row(120);
		Mat img7 = img1.col(220);

		img2 = ~img2; 

		imshow("Cat1", img1);
		imshow("Cat2", img2);
		imshow("cat3", img3);
		imshow("Cat4", img4);
		imshow("Cat5", img5);
		imshow("Cat6", img6);
		imshow("Cat7", img7);

		waitKey();
		destroyAllWindows();
	}
	
	//행렬의 원소 값 참조
	{
		Mat mat1 = Mat::zeros(300, 400, CV_8UC1);

		imshow("before", mat1);

		for (int j = 0; j < mat1.rows; j++) {
			for (int i = 0; i < mat1.cols; i++) {
				mat1.at<uchar>(j, i) += 100;
			}
		}
		imshow("after 1", mat1);

		for (int j = 0; j < mat1.rows; j++) {
			uchar* p = mat1.ptr<uchar>(j);
			for (int i = 0; i < mat1.cols; i++) {
				p[i] += 100;
			}
		}
		imshow("after 2", mat1);

		for (MatIterator_<uchar> it = mat1.begin<uchar>(); it != mat1.end<uchar>(); ++it) {
			(*it) += 55;
		}
		imshow("after 3", mat1);

		waitKey();
		destroyAllWindows();
	}

	//행렬 정보 참조하기
	{
		Mat img1 = imread("lenna.bmp");

		cout << "행렬 정보 참조" << endl;
		cout << "Width: " << img1.cols << endl;
		cout << "Height: " << img1.rows << endl;
		cout << img1.size() << endl;
	}
	return 0;
}