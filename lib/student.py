#!/usr/bin/env python

from user import User

class Student(User):
    
    def __init__(self):
        self.knowledge = []
    
    def learn(self,leared) -> str:
        self.knowledge.append(leared)
        return f"Leared : {leared}"
        pass
