program teste;
	var aux, aux1: integer;

	procedure fatorial(n : integer);
		begin
			n := 3;
			fatorial := n;
		end;
	
	procedure pot(n : integer);
		var aux, count : integer;
		begin
			aux := 1;
            for count := 0 to n - 1 do
            begin
                aux := aux * 10;
            end;
			pot := aux; 
		end;

begin
	aux := 1;
	fatorial(aux);
	pot(2);
	write(pot);
end
.
