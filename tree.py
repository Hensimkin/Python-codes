class Object:
   def __init__(self, key1):
      self.key = key1
      self.lc = []
      self.rc = []

   def insert(self, son):
      if son.key < self.key and len(self.lc) != 2:
         self.lc.append(son)
         if len(self.lc) == 2:
            self.sort_function(self.lc)
      elif son.key > self.key and len(self.rc) != 2:
         self.rc.append(son)
         if len(self.rc) == 2:
            self.sort_function(self.rc)
      elif son.key < self.key and len(self.lc) == 2:
         if son.key<self.lc[0].key:
            return self.lc[0].insert(son)
         elif self.lc[0].key < son.key < self.lc[1].key:
            return self.lc[0].insert(son) or self.lc[1].insert(son)
         elif self.lc[1].key < son.key < self.rc[0].key:
            return self.lc[1].insert(son)
      elif son.key > self.key and len(self.lc) == 2:
         if son.key > self.rc[1].key:
            return self.rc[1].insert(son)
         elif self.rc[0].key > son.key > self.lc[1].key:
            return self.rc[0].insert(son)
         elif self.rc[0].key < son.key < self.rc[1].key:
            return self.rc[0].insert(son) or self.rc[1].insert(son)

   def sort_function(self,array):
      if array == self.lc:
         if self.lc[0].key>self.lc[1].key:
            d=self.lc[0]
            f=self.lc[1]
            self.lc[0]=f
            self.lc[1]=d
      if array == self.rc:
         if self.rc[0].key>self.rc[1].key:
            d=self.rc[0]
            f=self.rc[1]
            self.rc[0]=f
            self.rc[1]=d

   def sons_print(self):
      for i in self.lc:
         print(i.key)
      for i in self.rc:
         print(i.key)




og=Object(10)
og1=Object(4)
og2=Object(2)
og3=Object(12)
og4=Object(14)
og5=Object(1)
og6=Object(55)
og.insert(og1)
og.insert(og2)
og.insert(og3)
og.insert(og4)
og.insert(og5)
og.insert(og6)




















