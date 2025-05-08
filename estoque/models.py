from datetime import datetime
from . import db

class Venda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, default=datetime.utcnow)
    total = db.Column(db.Float, nullable=False)
    desconto = db.Column(db.Float, default=0)
    metodo_pagamento = db.Column(db.String(20), nullable=False)
    troco = db.Column(db.Float, default=0.0)
    itens = db.relationship('ItemVenda', backref='venda', lazy=True)


class ItemVenda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
    venda_id = db.Column(db.Integer, db.ForeignKey('venda.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    preco_unitario = db.Column(db.Float, nullable=False)
