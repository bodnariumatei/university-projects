package com.sn.socialnetwork.utils;

public class Pair<T1, T2>{
    private T1 elem1;
    private T2 elem2;

    public Pair(T1 elem1, T2 elem2) {
        this.elem1 = elem1;
        this.elem2 = elem2;
    }

    public T1 getFirstId() {
        return elem1;
    }

    public T2 getSecondId() {
        return elem2;
    }

    @Override
    public boolean equals(Object obj) {
        if(this == obj) return true;
        if(!(obj instanceof Pair)) return false;
        Pair<T1, T2> o = (Pair) obj;
        return (elem1.equals(o.getFirstId()) && elem2.equals(o.getSecondId()))
                || (elem1.equals(o.getSecondId()) && elem2.equals(o.getFirstId()));
    }

    @Override
    public String toString() {
        return "First: " + elem1 + " - Second: " + elem2;
    }
}
