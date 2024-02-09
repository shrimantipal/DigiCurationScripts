data wcsday;
   infile 'a:ccsday.dat';
   filename wctrials 'a:ccsday.dat';
   input B1  B2  B3  B4  B5  B6  T1  T2  T3  T4  Y;
   pccday = log (Y/(1-Y));
      proc reg;
      model pccday = B1 B2 B3 B4 B5 B6 T2 T3 T4/noint;
   run;