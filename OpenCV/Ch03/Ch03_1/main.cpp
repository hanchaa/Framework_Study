#include "opencv2/opencv.hpp"
#include <iostream>

using namespace std;
using namespace cv;

int main() {
	// Point_ 클래스
	cout << "Point_ 클래스" << endl;

	Point pt1;
	pt1.x = 5; pt1.y = 10;

	Point pt2(10, 30);

	Point pt3 = pt1 + pt2;
	Point pt4 = pt1 * 2;

	Point pt5(pt1);

	int d1 = pt1.dot(pt2);
	bool b1 = (pt1 == pt2);

	cout << "pt1: " << pt1 << endl;
	cout << "pt5: " << pt5 << endl;

	cout << endl;

	// Size_ 클래스
	cout << "Size_ 클래스" << endl;

	Size sz1, sz2(10, 20);
	sz1.width = 5; sz1.height = 10;

	Size sz3 = sz1 + sz2;
	Size sz4 = sz1 * 2;
	int area1 = sz4.area();

	cout << "sz3: " << sz3 << endl;
	cout << "sz4: " << sz4 << endl;

	cout << endl;

	// Rect_ 클래스
	cout << "Rect_ 클래스" << endl;

	Rect rc1;
	Rect rc2(10, 10, 60, 40);

	Rect rc3 = rc1 + Size(50, 40);
	Rect rc4 = rc2 + Point(10, 10);

	Rect rc5 = rc3 & rc4;
	Rect rc6 = rc3 | rc4;

	cout << "rc5: " << rc5 << endl;
	cout << "rc6: " << rc6 << endl;

	cout << endl;

	//RotatedRect 클래스
	cout << "RotatedRect 클래스" << endl;

	RotatedRect rr1(Point2f(40, 30), Size2f(40, 20), 30.f);

	Point2f pts[10];
	rr1.points(pts);

	cout << pts[0] << pts[1] << pts[2] << pts[3] << pts[4] << endl;

	Rect br = rr1.boundingRect();
	cout << br << endl;

	Rect2f brf = rr1.boundingRect2f();
	cout << brf << endl;

	cout << endl;

	//Range 클래스
	cout << "Range 클래스" << endl;

	Range r1(0, 10);

	cout << r1 << endl;

	cout << endl;

	//String 클래스
	cout << "String 클래스" << endl;

	String str1 = "Hello";
	String str2 = "World";
	String str3 = str1 + " " + str2;

	cout << str3 << endl;

	cout << endl;
	
	return 0;
}