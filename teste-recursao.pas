program teste;
	var aux, aux1: integer;

	procedure fatorial(n : integer);
		begin
			if (n = 0 or n = 1) then
			begin
				aux := 1;
			end
			else
			begin
				fatorial(n-1)
				aux := n * aux
			end;
	// n aux 
	// 4  24
	// 3  6
	// 2  2 
	// 1  1
	// 1
		end;

begin
	aux := 1;
	fatorial(4);
end
.
