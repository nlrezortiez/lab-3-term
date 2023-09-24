	.file	"biquadratic_meta.cc"
	.intel_syntax noprefix
	.text
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"("
.LC1:
	.string	""
.LC3:
	.string	", "
.LC7:
	.string	")\n"
	.section	.text.startup,"ax",@progbits
	.p2align 4
	.globl	main
	.type	main, @function
main:
.LFB2503:
	.cfi_startproc
	sub	rsp, 8
	.cfi_def_cfa_offset 16
	mov	esi, OFFSET FLAT:.LC0
	mov	edi, OFFSET FLAT:_ZSt4cout
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	mov	esi, OFFSET FLAT:.LC1
	mov	edi, OFFSET FLAT:_ZSt4cout
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	movsd	xmm0, QWORD PTR .LC2[rip]
	mov	rdi, rax
	call	_ZNSo9_M_insertIdEERSoT_
	mov	esi, OFFSET FLAT:.LC3
	mov	edi, OFFSET FLAT:_ZSt4cout
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	movsd	xmm0, QWORD PTR .LC4[rip]
	mov	rdi, rax
	call	_ZNSo9_M_insertIdEERSoT_
	mov	esi, OFFSET FLAT:.LC3
	mov	edi, OFFSET FLAT:_ZSt4cout
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	movsd	xmm0, QWORD PTR .LC5[rip]
	mov	rdi, rax
	call	_ZNSo9_M_insertIdEERSoT_
	mov	esi, OFFSET FLAT:.LC3
	mov	edi, OFFSET FLAT:_ZSt4cout
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	movsd	xmm0, QWORD PTR .LC6[rip]
	mov	rdi, rax
	call	_ZNSo9_M_insertIdEERSoT_
	mov	esi, OFFSET FLAT:.LC7
	mov	edi, OFFSET FLAT:_ZSt4cout
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	xor	eax, eax
	add	rsp, 8
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE2503:
	.size	main, .-main
	.p2align 4
	.type	_GLOBAL__sub_I_main, @function
_GLOBAL__sub_I_main:
.LFB3203:
	.cfi_startproc
	sub	rsp, 8
	.cfi_def_cfa_offset 16
	mov	edi, OFFSET FLAT:_ZStL8__ioinit
	call	_ZNSt8ios_base4InitC1Ev
	mov	edx, OFFSET FLAT:__dso_handle
	mov	esi, OFFSET FLAT:_ZStL8__ioinit
	mov	edi, OFFSET FLAT:_ZNSt8ios_base4InitD1Ev
	add	rsp, 8
	.cfi_def_cfa_offset 8
	jmp	__cxa_atexit
	.cfi_endproc
.LFE3203:
	.size	_GLOBAL__sub_I_main, .-_GLOBAL__sub_I_main
	.section	.init_array,"aw"
	.align 8
	.quad	_GLOBAL__sub_I_main
	.local	_ZStL8__ioinit
	.comm	_ZStL8__ioinit,1,1
	.section	.rodata.cst8,"aM",@progbits,8
	.align 8
.LC2:
	.long	0
	.long	1075314688
	.align 8
.LC4:
	.long	0
	.long	1073741824
	.align 8
.LC5:
	.long	0
	.long	-1072168960
	.align 8
.LC6:
	.long	0
	.long	-1073741824
	.hidden	__dso_handle
	.ident	"GCC: (GNU) 12.3.0"
	.section	.note.GNU-stack,"",@progbits
