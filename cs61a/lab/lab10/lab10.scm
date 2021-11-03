(define (over-or-under num1 num2) 
     (if (< num1 num2) (- 0 1)
         (if (= num1 num2) 0
              1))
  )

(define (make-adder num)
      (lambda (inc) (+ num inc))
  )

(define (composed f g) 
      (lambda (x) (f(g x)))
  )

(define lst
  (cons (cons 1 nil) 
        (cons 2 
              (cons
                    (cons 3 (cons 4 nil))
                    (cons 5 nil)
                  
              )
          )
      )
  )

(define (remove item lst) 'YOUR-CODE-HERE)
