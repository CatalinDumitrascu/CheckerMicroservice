package org.example;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class AddTest {

    @Test
    void add() {

        var calculator = new Main();
        assertEquals(4, calculator.add(2,2));
    }
}