from tournament import Tournament
class Nodo:
  def __init__(self,info,):
        self.info= info
        self.izq= None
        self.der= None

  def get_info(self):
      return self.info
  
  def get_izq(self):
      return self.izq
  
  def get_der(self):
      return self.der

  def set_info(self,info):
      self.info= info

  def set_izq(self,izq):
      self.izq= izq

  def set_der(self,der):
      self.der= der

  def set_partido(self,partido):
      self.partido= partido


  def agregar(self,raiz,info):
      if raiz is not None:
          if info < raiz.get_info():
              if raiz.get_izq() is None:
                 raiz.set_izq(Nodo(info)) 
              else:
                  self.agregar(raiz.get_izq(),info)
          if info > raiz.get_info():
              if raiz.get_der() is None:
                  raiz.set_der(Nodo(info))
              else:
                  self.agregar(raiz.get_der(), info)
          return raiz 
      else:
          return None
      
  def in_order(self,raiz):
      if raiz is not None:
       self.in_order(raiz.get_izq())
       print(raiz.get_info(),end=" ") 
       self.in_order(raiz.get_der())

  def pre_order(self, raiz):
    if raiz is not None:
      print(raiz.get_info(),end=" ") 
      self.in_order(raiz.get_izq())
      self.in_order(raiz.get_der())

  def post_order(self,raiz):
    if raiz is not None:
      self.in_order(raiz.get_izq())
      self.in_order(raiz.get_der())
      print(raiz.get_info(),end=" ")

  def altura(self,raiz):
     if raiz is None:
        return 0
     else:
        return max(self.altura(raiz.get_izq())+1, self.altura(raiz.get_der())+1)
     
  def peso(self,raiz):
     if raiz is None:
        return 0
     else:
        return 1 + self.peso(raiz.get_izq())+ self.peso(raiz.get_der)

  def valor_maximo(self,raiz):
     if raiz.get_der() is None:
        return raiz.get_info()
     else:
        return self.valor_maximo(raiz.get_der())
     
  def existe_nodo(self,raiz,info):
     if raiz is None:
      return False
     else:
       if raiz.get_info()== info:
         return True
       else:
         return self.existe_nodo(raiz.get_izq()) or self.existe_nodo(raiz.get_der())
       
  def is_arbol(self,raiz):
     if raiz is not None:
        return True
     
     if raiz.get_info() > raiz.get_der().get_info() or  raiz.get_info() < raiz.get_izq().get_info():
            return False
     
     return True and self.is_arbol(raiz.get_der()) and self.is_arbol(raiz.get_izq())
  
  def construir_arbol(self,raiz,info):
     if raiz is not None and len(info) != 0:
        
        if self.altura(raiz) == 1:
            raiz.set_info(info[0])
            del info[0]
            
        else:
           self.construir_arbol(raiz.get_der(),info)
           self.construir_arbol(raiz.get_izq(),info)

  def construir_arbol2(self,raiz,info):
     if raiz is not None:
        if self.altura(raiz) == 2:
            
            raiz.set_info((info[0]))
            del info[0]
            
        else:
           self.construir_arbol2(raiz.get_der(),info)
           self.construir_arbol2(raiz.get_izq(),info)

  def construir_arbol3(self,raiz,info):
     if raiz is not None:
        if self.altura(raiz) == 3:
            raiz.set_info((info[0]))
            del info[0]
            
        else:
           self.construir_arbol3(raiz.get_der(),info)
           self.construir_arbol3(raiz.get_izq(),info)


        
           

        
raiz= Nodo(8)
raiz= raiz.agregar(raiz,4)
raiz= raiz.agregar(raiz,12)
raiz= raiz.agregar(raiz,2)
raiz= raiz.agregar(raiz,6)
raiz= raiz.agregar(raiz,10)
raiz= raiz.agregar(raiz,14)
raiz= raiz.agregar(raiz,1)
raiz= raiz.agregar(raiz,3)
raiz= raiz.agregar(raiz,5)
raiz= raiz.agregar(raiz,7)
raiz= raiz.agregar(raiz,9)
raiz= raiz.agregar(raiz,11)
raiz= raiz.agregar(raiz,13)
raiz= raiz.agregar(raiz,15)

T= Tournament()
clasificados=[("colombia","peru"),("francia","argentina"),("españa","belgica"),("ecuador","jamaica"),("mexico","irlanda"),("chile","japon"),("corea del sur","EEUU"),("brasil","portugal")]
