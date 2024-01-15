// https://www.codewars.com/kata/56c04261c3fcf33f2d000534


double doubles(int maxk, int maxn) {
  double s = 0;

  for (int i = 1; i < maxk + 1; i++){
    for (int j = 1; j < maxn +1; j++){
      s += 1/(i * pow(j+1, 2*i));
    }
  }
	return s;
}
