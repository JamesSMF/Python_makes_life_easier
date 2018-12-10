on pAS(A, i, B)
	if i < 1 then
		log B
		return
	end if
	
	set addedItem to item i of A
	set C to addedItem & B
	pAS(A, i - 1, C)
	set C to B
	pAS(A, i - 1, C)
end pAS

set B to {}
set A to {1, 2, 3, 4}
set i to the length of A
pAS(A, i, B)
