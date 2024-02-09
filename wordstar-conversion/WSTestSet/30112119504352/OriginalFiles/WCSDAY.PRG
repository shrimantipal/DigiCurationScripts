data wcsday;
   infile 'a:wcsday.dat';
   filename wctrials 'a:wcsday.dat';
   input B1  B2  B3  B4  B5  B6  T1  T2  T3  T4  Y;
   pnit = log (Y/(1-Y));
      proc reg;
      model pnit = B1 B2 B3 B4 B5 B6 T2 T3 T4/noint;
   run;