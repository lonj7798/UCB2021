(define (cddr s) (cdr (cdr s)))

(define (cadr s) 
    (car (cdr s))
  )

(define (caddr s)
    (car (cdr (cdr s)))
  )

(define (ordered? s)
    (if (> (car s) (cadr s)) #f 
        (if (null? (cdr (cdr s))) #t
            (ordered? (cdr s))))
  )

(define (square x) (* x x))

(define (pow base exp)
  (if (= exp 1) base
      (if (even? exp) (square (pow base (/ exp 2)))
          (* base (square (pow base (/ (- exp 1) 2))))
          )
      )
  )


