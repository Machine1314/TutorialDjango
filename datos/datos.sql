----Tutorial
do $$
begin
   for cnt in 1..10 loop
    INSERT INTO public."Filtrado_equipolab"(codigo, nombre)
	VALUES (cnt, 'Equipo#' || cast(cnt as varchar));
   end loop;
end; $$

do $$
begin
   for cnt in 1..10 loop
    INSERT INTO public."Filtrado_prestamo"(
	codigo, estado, "fechaInicio", "fechaFin", "fechaEntrega", usuario, equipo_id)
	VALUES (cnt, 'PRESTADO', now()::date, now()::date + cnt, null, 'bduenas', cnt);
   end loop;
end; $$