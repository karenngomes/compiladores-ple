program teste;
	var entrada: integer;

  function fat(n:integer) : integer;
  begin
    if (n <= 1) then
      begin
        fat := 1;
      end
    else
      begin
        fat(n - 1);
        fat := n * fat;
      end;
  end;

  function fibo(n:integer): integer;
    var aux : integer;
  begin
    if (n <= 1) then
      begin
        fibo := n;
      end
    else
      begin
        fibo(n-1);
        aux := fibo;
        fibo(n-2);
        fibo := aux + fibo;
      end;
  end;

  procedure myprint(n, m: integer);
  begin
    write(n);
    write(m);
  end;

begin
  fat(3);
  write(fat);
  fibo(4);
  write(fibo);
  myprint(3, 4);
end.
