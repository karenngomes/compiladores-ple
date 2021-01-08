program teste;
	var entrada, entrada2, aux, result, limiter, limiter2: integer;

begin
  limiter := 0;
  limiter2 := 1;
  repeat
    write(limiter2, limiter2, limiter2, limiter2, limiter2, limiter2, limiter2);
    read(aux);
    if (aux > 0) then
      begin
        write(limiter, limiter, limiter, limiter, limiter, limiter, limiter);
        read(entrada, entrada2);
        write(limiter, limiter, limiter, limiter, limiter, limiter, limiter);

        if (aux = 1) then
          begin
            result := entrada + entrada2;
          end
        else
          begin
            if (aux = 2) then
              begin
                result := entrada - entrada2;
              end
            else
              begin
                if (aux = 3) then
                  begin
                    result := entrada * entrada2;
                  end
                else
                  begin
                    if (aux = 4) then
                      begin
                        result := entrada / entrada2;
                      end
                    else
                      begin
                        result := 0 - 127;
                      end;
                  end;
              end;
          end;
        write(result);
      end;
  until(aux = 0);
end.
