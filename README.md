# 208dowels

A power hammer mass produces dowels. Sometimes, some pieces are defective, and the whole process requires quality control: 100 samples of 100 pieces are randomly taken, and defective pieces are numbered. We get what we call an observed serial. Then, a statistical fit is done using the binomial distribution, and validated using the χ2 test.

Let’s note x the number of defective pieces, Oxthe size of the observed sample, and Txthe theoretical size. To ensure the consistency of the fit, statistical classes which have less than 10 elements are merged until there are only classes with 10 or more elements. Smallest classes are aggregated first.

Finally, with the number of constraints for the fit being 2, the degrees of freedom parameter ν is equal to the number of classes minus 2.

Your program will take 9 integers as inputs, representing respectively O0, O1,. . . ,O8+ and will output:

1. an array showing observed and theoretical sizes for each statistical class (with totals)

2. the chosen probability distribution for the fit,

3. the value of χ2,

4. the value of ν,

5. the value range in which the probability falls if the fit is valid.

## Compile

The project compile with *Makefile*:

For compile the project use the commande:

```console
foo@bar:~/208dowels$ make re
```

For clean the project use:

```console
foo@bar:~/208dowels$ make fclean
```

Get instruction with:


```console
foo@bar:~/208dowels$ ./208dowels -h
```

Launch test with:

```console
foo@bar:~/208dowels$ make test
foo@bar:~/208dowels$ ./unit_test
```

## x² distribution table


|ν  |   99%  | 90%  |   80%  | 70%  |   60%  | 50%  |   40%  | 30%  |   20%  | 10%  |   5%   | 2%    |  1%|
|--:	|:-:	|---	|--:	|--:	|---	|---	|---	|---	|---	|---	|---	|---	|---	|
|1      |0.00    |0.02      |0.06    |0.15      |0.27    |0.45      |0.71    |1.07      |1.64    |2.71      |3.84    |5.41      |6.63|
|2      |0.02    |0.21      |0.45    |0.71      |1.02    |1.39      |1.83    |2.41      |3.22    |4.61      |5.99    |7.82      |9.21|
|3      |0.11    |0.58       |1.01          |1.42        |1.87    |2.37         |2.95      |3.66      |4.64    |6.25       |7.81          |9.84        |11.34|
|4      |0.30    |1.06       |1.65          |2.19        |2.75    |3.36         |4.04      |4.88      |5.99    |7.78       |9.49          |11.67       |13.28|
|5      |0.55    |1.61       |2.34          |3.00        |3.66    |4.35         |5.13      |6.06      |7.29    |9.24       |11.07         |13.39           |15.09|
|6      |0.87    |2.20       |3.07          |3.83        |4.57    |5.35         |6.21      |7.23      |8.56    |10.64      |12.59     |15.03       |16.81|
|7      |1.24    |2.83       |3.82          |4.67        |5.49    |6.35         |7.28      |8.38      |9.80    |12.02      |14.07     |16.62       |18.48|
|8      |1.65    |3.49       |4.59          |5.53        |6.42    |7.34         |8.35      |9.52      |11.03       |13.36      |15.51         |18.17      |20.09|
|9      |2.09    |4.17       |5.38          |6.39        |7.36    |8.34         |9.41      |10.66     |12.24       |14.68  |16.92        |19.68   |21.67|
|10     |2.56        |4.87       |6.18     |7.27     |8.30          |9.34       |10.47  |11.78        |13.44   |15.99     |18.31    |21.16      |23.21|

## Example

![image](asset/example.png)
