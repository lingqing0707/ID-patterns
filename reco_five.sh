#!/bin/bash
a=Valid.
b=0
c=256
echo "=============================================================="
for ((x=0;x<16;x++)) do
	for ((y=0;y<16;y++)) do
		for ((g=0;g<16;g++)) do
			for ((h=0;h<16;h++)) do
				python3 reco_five.py $x $y $g $h
				result=`stp normal_IDC.cvc`
				result1=`stp specific_IDC.cvc`
				if [[ "$result" != "$a" ]] && [[ "$result1" = "$a" ]]; then
					let b+=1
					wx=`echo "obase=2;$x" | bc`
					ux=`echo $wx | awk '{printf("%04d\n",$0)}'`
					wy=`echo "obase=2;$y" | bc`
					uy=`echo $wy | awk '{printf("%04d\n",$0)}'`
					wg=`echo "obase=2;$g" | bc`
					ug=`echo $wg | awk '{printf("%04d\n",$0)}'`
					wh=`echo "obase=2;$h" | bc`
					uh=`echo $wh | awk '{printf("%04d\n",$0)}'`
					echo "current IDC-pattern (Δx, Δy, Δg → Δh): ($ux*, $uy*, $ug* → $uh*)"
				fi
			done
		done
	done
done
echo "=============================================================="
echo "count number: $b"
